import re
from dataset import documents, topic_keywords

STOP_WORDS = {
    "what", "is", "are", "the", "a", "an", "of", "for",
    "to", "in", "and", "how", "does", "do", "explain",
    "describe", "tell", "me", "about", "which", "when",
    "why", "can", "you", "please", "give", "define",
    "with", "on", "it", "this", "that", "be", "by",
    "difference", "between", "compare", "comparison",
    "show", "meaning"
}

SYNONYMS = {
    "deadlocks": "deadlock",
    "schedules": "scheduling",
    "schedule": "scheduling",
    "threads": "thread",
    "processes": "process",
    "files": "file",
    "directories": "directory",
    "faults": "fault",
    "frames": "frame",
    "pages": "page",
    "semaphores": "semaphore",
    "mutexes": "mutex",
    "algorithms": "algorithm",
    "allocations": "allocation",
    "synchronized": "synchronization",
    "synchronizing": "synchronization",
    "synchronize": "synchronization",
    "rr": "round",
    "systems": "system"
}

def get_words(text):
    words = re.findall(r"[a-zA-Z]+", text.lower())
    return {
        SYNONYMS.get(word, word)
        for word in words
        if word not in STOP_WORDS
    }

def answer_question(question):
    question_lower = question.lower().strip()
    question_words = get_words(question)

    if question_lower in {"os", "o.s", "operating system"}:
        return (
            "An Operating System (OS) manages computer hardware, memory, "
            "files, processes, and devices. It provides an interface between "
            "users, applications, and hardware.",
            "Operating System Basics",
            5
        )

    if not question_words:
        return "Please enter a meaningful Operating Systems question.", "None", 0

    if "physics" in question_words or "chemistry" in question_words:
        return (
            "This question is outside my Operating Systems knowledge base.",
            "None",
            0
        )

    if "process" in question_words and "thread" in question_words:
        return (
            "A process is an independent program in execution, while a thread "
            "is a unit of execution within a process. Each process generally "
            "has its own address space. Threads within the same process share "
            "memory and other resources. Creating threads is generally less "
            "costly than creating separate processes.",
            "CPU and Process Concepts",
            5
        )

    topic_scores = {}

    for topic, sentences in documents.items():
        content_words = get_words(" ".join(sentences))
        keyword_set = topic_keywords[topic]
        content_matches = question_words & content_words
        keyword_matches = question_words & keyword_set
        score = len(content_matches) + 2 * len(keyword_matches)

        if topic == "Operating System Basics" and (
            "os" in question_lower or "operating" in question_words
        ):
            score += 5

        topic_scores[topic] = score

    ranked_topics = sorted(
        topic_scores.items(),
        key=lambda item: item[1],
        reverse=True
    )

    best_topic, best_score = ranked_topics[0]
    second_score = ranked_topics[1][1]

    if best_score < 2:
        return "No relevant OS topic found. Please try another question.", "None", 0

    if best_score == second_score:
        return (
            "Your question matches multiple topics. Please rephrase it or "
            "include a specific keyword.",
            "None",
            best_score
        )

    if best_score - second_score < 2:
        return (
            "No confident topic match found. Please rephrase your question.",
            "None",
            best_score
        )

    scored_sentences = []

    for sentence in documents[best_topic]:
        sentence_score = len(question_words & get_words(sentence))
        if sentence_score > 0:
            scored_sentences.append((sentence_score, sentence))

    scored_sentences.sort(key=lambda item: item[0], reverse=True)
    selected_sentences = [
        sentence for score, sentence in scored_sentences[:3]
    ]

    if not selected_sentences:
        return "No relevant answer found. Please rephrase your question.", "None", 0

    return " ".join(selected_sentences), best_topic, best_score
