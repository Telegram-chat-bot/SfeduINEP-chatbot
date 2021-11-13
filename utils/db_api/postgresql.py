from asyncpg import Pool
from typing import Union

from asyncpg.connection import Connection
# from data import config
import asyncpg
import asyncio


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create_connection(self):
        self.pool = await asyncpg.create_pool(
            user="postgres",
            password="860269",
            host="127.0.0.1",
            database="chat-bot-data",
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
    

    async def get_data(self, block, element):
        sql = f"""
        SELECT {element} FROM {block}
        """
        return await self.execute(sql, fetchval=True)

    async def get_directions(self, block, level):
        sql = f"""
        SELECT direction, name_of_dir, inf  FROM {block} WHERE level='{level}'
        """
        return await self.execute(sql, fetch=True)

    async def get_id(self, direct, code):
        sql = f"""
        SELECT id, direction, name_of_dir FROM {direct};
        """
        return await self.execute(sql, fetch=True)
    
    async def get_passing_scores(self, block, id):
        sql = f"""
        SELECT inf FROM {block} WHERE direction_id='{id}'
        """
        return await self.execute(sql, fetch=True)

        
    # async def add_data(self, inf, block, element):
    #     sql = f"""
    #     INSERT INTO {block}
    #         ({element})
    #     SELECT '{inf}'
    #     WHERE
    #         NOT EXISTS (
    #             SELECT {element} FROM {block}
    # );
    #     """
    #     return await self.execute(sql, execute=True)

    # async def update_data(self, block, element, inf):
    #     sql = f"""
    #     UPDATE {block} SET {element} = '{inf}'
    #     """
    #     return await self.execute(sql, execute=True)

# db = Database()
# loop = asyncio.get_event_loop()
# loop.run_until_complete(db.create_connection())
# print(loop.run_until_complete(db.get_directions(block="bot_directions", level="spec")))
# r = loop.run_until_complete(db.get_id(direct="bot_directions", code="09.04.03"))
# print(loop.run_until_complete(db.get_passing_scores(block="bot_num_places", id=r[0].get('id')))[0].get('inf'))
