from rag_engine import get_knowledge_base, retrieve_documents, generate_answer


def main():
    knowledge_base = get_knowledge_base()

    question = input(
        "\nAsk an Operating Systems question: "
    ).strip()

    if not question:
        print("Please enter a question.")
        return

    results = retrieve_documents(question, knowledge_base)

    print("\nRetrieved passages:\n")

    for result in results:
        print(f"Topic: {result['topic']}")
        print(f"Similarity: {result['score']:.4f}")
        print(f"Passage: {result['text']}")
        print("-" * 60)

    print("\nOSLabAI Answer:\n")

    if not results:
        print(
            "I can only answer questions related to Operating Systems. "
            "Please ask an OS-related question."
        )
    else:
        print(generate_answer(question, results))


if __name__ == "__main__":
    main()
