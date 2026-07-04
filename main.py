import asyncio

from dotenv import load_dotenv
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

from config import config
from llm.factory import get_llm
from observability import logger
from agent.factory import build_agent


console = Console()


async def ask_llm(llm, question: str) -> str:
    """
    Send a question to the configured LLM.
    """
    logger.info("Sending request to LLM")

    response = await llm.ainvoke(question)

    logger.info("Received response from LLM")

    return response.content


async def main():
    # Load environment variables
    load_dotenv()

    logger.info("Application started")
    logger.info("Configuration loaded")

    llm = get_llm()
    logger.info("LLM initialized")

    console.print(
        Panel.fit(
            "[bold cyan]AI Assistant[/bold cyan]\n\n"
            "Commands:\n"
            "• /ask <question>\n"
            "• exit",
            title="Welcome",
        )
    )

    while True:
        try:
            user_input = Prompt.ask("[bold green]>[/bold green]").strip()

            # Skip empty input
            if not user_input:
                continue

            # Exit
            if user_input.lower() == "exit":
                logger.info("Application terminated by user")
                console.print("[bold yellow]Goodbye! 👋[/bold yellow]")
                break

            # Validate command
            if not user_input.startswith("/ask"):
                console.print(
                    "[bold red]Invalid command.[/bold red] Use [cyan]/ask <question>[/cyan]"
                )
                continue

            question = user_input[4:].strip()

            if not question:
                console.print("[yellow]Please enter a question.[/yellow]")
                continue

            logger.info(f"Question: {question}")

            with console.status(
                "[bold cyan]Thinking...[/bold cyan]",
                spinner="dots",
            ):
                answer = await ask_llm(llm, question)

            console.print("\n[bold blue]AI:[/bold blue]")
            console.print(answer)
            console.print()

        except KeyboardInterrupt:
            logger.info("KeyboardInterrupt received")
            console.print("\n[yellow]Exiting...[/yellow]")
            break

        except Exception:
            logger.exception("Unexpected error")
            console.print("[bold red]An unexpected error occurred.[/bold red]")


if __name__ == "__main__":
    asyncio.run(main())