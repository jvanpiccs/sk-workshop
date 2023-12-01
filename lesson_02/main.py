import semantic_kernel as sk
from plugins.CallCenterPlugin.Transcribe import Transcribe


async def main():
    # Initialize the kernel
    kernel = sk.Kernel()
    # Add a text or chat completion service using either:
    # kernel.add_text_completion_service()
    # kernel.add_chat_service()

    # Import the MathPlugin.
    math_plugin = kernel.import_skill(Transcribe(), skill_name="CallCenterPlugin")

    # Run the Sqrt function with the context.
    result = await kernel.run_async(
        math_plugin["Sqrt"],
        input_str="12",
    )

    print(result)


# Run the main function
if __name__ == "__main__":
    import asyncio

    asyncio.run(main())