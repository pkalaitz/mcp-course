from dotenv import load_dotenv
import asyncio
load_dotenv()
async def main():  # make it co-routine
    print("Hello from mcp-crash-course!")


if __name__ == "__main__":
    asyncio.run(main())
