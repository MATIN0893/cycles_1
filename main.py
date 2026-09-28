import asyncio

async def main():
    print("Cycle 1 executed")
    # Run loop once
    for i in range(1):
        print(f"Iteration {i+1}")
        await asyncio.sleep(0)  # no-op

if __name__ == "__main__":
    asyncio.run(main())