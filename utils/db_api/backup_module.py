import logging
from datetime import datetime
from data import config
from django_admin.django_admin.settings import ROOT_DIR

import os
import sys


class DatabaseDump:
	__dbname: str = config.DB_NAME
	__host: str = config.DB_HOST
	__user: str = config.DB_USER
	__password: str = config.DB_PASS
	__dump_path: str = os.path.join(ROOT_DIR, "data\\dumps")

	@staticmethod
	async def make_dump():
		if sys.platform in "linux":
			file_path = os.path.join(DatabaseDump.__dump_path, "db.dump")
			dump_status = os.WEXITSTATUS(os.system(
				f"pg_dump -h {DatabaseDump.__host} -U {DatabaseDump.__user} {DatabaseDump.__dbname} > {file_path}"
			))
			if dump_status != 0:
				logging.error(f"Не удалось создать резервную копию базы данных\n{dump_status}")
			else:
				logging.info(f"{datetime.now()} - копия базы данных успешно создана")
