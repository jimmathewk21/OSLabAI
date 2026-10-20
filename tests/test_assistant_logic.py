
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


    def test_processes_waiting_for_each_other(self):
        answer, topic, score = answer_question(
            "Why can processes wait forever for resources held by each other?"
        )
        self.assertEqual(topic, "Deadlocks")
        self.assertIn("deadlock", answer.lower())

    def test_ram_divided_into_pages_and_frames(self):
        answer, topic, score = answer_question(
            "How does paging divide memory into pages and frames?"
        )
        self.assertEqual(topic, "Memory Management")
        self.assertIn("page", answer.lower())
        self.assertIn("frame", answer.lower())

    def test_shared_data_access(self):
        answer, topic, score = answer_question(
            "What happens when two processes access shared data together?"
        )
        self.assertEqual(topic, "Process Synchronization")
        self.assertIn("race condition", answer.lower())
if __name__ == "__main__":
    unittest.main()
