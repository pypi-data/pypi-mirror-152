import os

from webdriver_manager.core.manager import DriverManager
from webdriver_manager.drivers.opera import OperaDriver


class OperaDriverManager(DriverManager):
    def __init__(
        self,
        version="latest",
        os_type=None,
        path=None,
        name="operadriver",
        url="https://github.com/operasoftware/operachromiumdriver/"
        "releases/",
        latest_release_url="https://api.github.com/repos/"
        "operasoftware/operachromiumdriver/releases/latest",
        opera_release_tag="https://api.github.com/repos/"
        "operasoftware/operachromiumdriver/releases/tags/{0}",
        cache_valid_range=1,
        download_manager=None,
    ):
        super().__init__(path, cache_valid_range, download_manager=download_manager)

        self.driver = OperaDriver(
            name=name,
            version=version,
            os_type=os_type,
            url=url,
            latest_release_url=latest_release_url,
            opera_release_tag=opera_release_tag,
            http_client=self.http_client,
        )

    def install(self):
        driver_path = self._get_driver_path(self.driver)
        if not os.path.isfile(driver_path):
            for name in os.listdir(driver_path):
                if "sha512_sum" in name:
                    os.remove(os.path.join(driver_path, name))
                    break
        driver_path = os.path.join(driver_path, os.listdir(driver_path)[0])
        os.chmod(driver_path, 0o755)
        return driver_path
