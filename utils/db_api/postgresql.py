from asyncpg import Pool
from typing import Union

from asyncpg.connection import Connection
from data import config
# import config
import asyncpg
# import asyncio


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create_connection(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DP_HOST,
            database=config.DB_NAME,
            max_inactive_connection_lifetime=3
        )
    
    async def execute(self, command, *args,
                    fetch: bool = False,
                    fetchval: bool = False,
                    fetchrow: bool = False,
                    execute: bool = False,
                    execute_many: bool = False):

        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
                elif execute_many:
                    result = await connection.executemany
                return result

    async def create_data_tables(self):
        sql = """
        CREATE TABLE IF NOT EXISTS admission (
            admission_rules TEXT,
            submit_doc TEXT,
            passing_scores TEXT,
            number_of_places TEXT,
            achievements TEXT,
            special_rights TEXT,
            admission_stat TEXT,
            enrollment_proc TEXT
        );

        CREATE TABLE IF NOT EXISTS About (
            acquaintance TEXT,
            excursion TEXT,
            events TEXT,
            science TEXT,
            partners_work TEXT,
            stud_council TEXT,
            photo TEXT,
            contacts TEXT,
            map TEXT
        );

        CREATE TABLE IF NOT EXISTS questions(FAQ TEXT)
        """
        return await self.execute(sql, execute=True)

    async def add_data(self, inf, block, element):
        sql = f"""
        INSERT INTO {block}
            ({element})
        SELECT '{inf}'
        WHERE
            NOT EXISTS (
                SELECT {element} FROM {block}
    );
        """
        return await self.execute(sql, execute=True)

    async def update_data(self, block, element, inf):
        sql = f"""
        UPDATE {block} SET {element} = '{inf}'
        """
        return await self.execute(sql, execute=True)

    async def get_data(self, block, element):
        sql = f"""
        SELECT {element} FROM {block}
        """
        return await self.execute(sql, fetchval=True)

    async def get_datas(self, block):
        sql = f"""
        SELECT * FROM {block}
        """
        return await self.execute(sql, fetchrow=True)


# db = Database()
# loop = asyncio.get_event_loop()
# loop.run_until_complete(db.create_connection())
# d = loop.run_until_complete(db.get_data(block="admission", element="admission_rules"))
# print(d)
# d = loop.run_until_complete(db.get_data(block="admission", element="admission_rules"))
# print(d[0].get("admission_rules"))