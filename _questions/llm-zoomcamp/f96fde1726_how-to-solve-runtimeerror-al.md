---
course: llm-zoomcamp
id: f96fde1726
question: 'How to Solve "RuntimeError: Already running asyncio in this thread"'
section: 'Workshops: Agents'
sort_order: 900
---

Jupyter notebooks already run an event loop in the main thread to handle asynchronous code. For this reason, when you try to call asyncio.run() inside a cell, you get the following error:

RuntimeError: asyncio.run() cannot be called from a running event loop

Instead of using asyncio.run(), simply use await directly in the notebook cell.

Incorrect:

import asyncio

async def main():

async with Client(weather_server.mcp) as mcp_client:

# your code here

# This will cause the RuntimeError

result = asyncio.run(main())

Correct:

async def main():

async with Client(weather_server.mcp) as mcp_client:

# your code here

# Use await directly

result = await main()

Jupyter notebooks automatically create an asyncio event loop when they start. Since asyncio.run() attempts to create a new event loop, it conflicts with the existing loop. By using await directly, you leverage the already running event loop.

Added by Marcelo Nieva

