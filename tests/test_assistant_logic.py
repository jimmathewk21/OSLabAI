
import unittest

from assistant_logic import answer_question


class TestOSLabAI(unittest.TestCase):

    def test_round_robin_scheduling(self):
        answer, topic, score = answer_question(
            "What is Round Robin scheduling?"
        )
        self.assertEqual(topic, "Process Scheduling")
        self.assertIn("time quantum", answer.lower())
        self.assertGreater(score, 0)

    def test_deadlock_conditions(self):
        answer, topic, score = answer_question(
            "Explain the four conditions for deadlock."
        )
        self.assertEqual(topic, "Deadlocks")
        self.assertIn("mutual exclusion", answer.lower())
        self.assertIn("circular wait", answer.lower())

    def test_page_fault(self):
        answer, topic, score = answer_question(
            "What happens when a page fault occurs?"
        )
        self.assertEqual(topic, "Memory Management")
        self.assertIn("physical memory", answer.lower())

    def test_semaphore(self):
        answer, topic, score = answer_question(
            "How does a semaphore work?"
        )
        self.assertEqual(topic, "Process Synchronization")
        self.assertIn("resource", answer.lower())

    def test_paging_vs_segmentation(self):
        answer, topic, score = answer_question(
            "What is the difference between paging and segmentation?"
        )
        self.assertEqual(topic, "Memory Management")
        self.assertIn("paging", answer.lower())
        self.assertIn("segmentation", answer.lower())

    def test_unrelated_question(self):
        answer, topic, score = answer_question(
            "How do I bake a chocolate cake?"
        )
        self.assertEqual(topic, "None")
        self.assertIn("no relevant os topic found", answer.lower())


if __name__ == "__main__":
    unittest.main()
