import os
import sys
from pathlib import Path

from data import config
from django_admin.django_admin.settings import ROOT_DIR


class RestoreDatabase:
	__dbname: str = config.DB_NAME
	__host: str = config.DB_HOST
	__user: str = config.DB_USER
	__password: str = config.DB_PASS
	__dump_path: str = os.path.join(ROOT_DIR, "data\\dumps")


	def __find_dump(self) -> bool:
		return not os.listdir("C:\\Users\\Артём\\Проекты\\INEP_Telegram_Bot\\data\\dumps")

	def get_file(self, file: str):
		if self.__find_dump():
			return Path(os.path.join("C:\\Users\\Артём\\Проекты\\INEP_Telegram_Bot\\data\\dumps", file)).is_file()

	def run_restore(self, file_dump: str):
		if sys.platform in "linux":
			restore_status = os.WEXITSTATUS(os.system(
				f"pg_restore -h {RestoreDatabase.__host} -U {RestoreDatabase.__user} {RestoreDatabase.__dbname} < {file_dump}"
			))

if __name__ == "__main__":
	f = RestoreDatabase()
	print(f.get_file("f.txt"))