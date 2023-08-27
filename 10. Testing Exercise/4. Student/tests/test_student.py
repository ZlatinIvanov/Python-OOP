from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):

    def setUp(self) -> None:

        self.student = Student("Student1")
        self.student_with_courses = Student("Student2", {"python": ["some note"]})

    def test_correct_initialization(self):

        self.assertEqual("Student1", self.student.name)
        self.assertEqual("Student2", self.student_with_courses.name)
        self.assertEqual({"python": ["some note"]}, self.student_with_courses.courses)

    def test_enroll_and_add_notes_to_existing_course(self):

        result = self.student_with_courses.enroll("python", ["python is cool"])

        self.assertEqual(["some note", "python is cool"], self.student_with_courses.courses["python"])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_and_add_notes_to_non_existing_course_without_third_param(self):

        result = self.student.enroll("java", ["java is hard"])

        self.assertEqual(["java is hard"], self.student.courses["java"])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_and_add_notes_to_non_existing_course_with_third_param_Y(self):

        result = self.student.enroll("java", ["java is hard"], "Y")

        self.assertEqual(["java is hard"], self.student.courses["java"])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_and_add_new_course_without_adding_the_notes(self):

        result = self.student.enroll("java", ["java is hard"], "n")

        self.assertEqual([], self.student.courses["java"])
        self.assertEqual("Course has been added.", result)

    def test_add_notes_to_existing_course(self):

        self.assertEqual("Notes have been updated", self.student_with_courses.add_notes("python", "DB"))

    def test_add_notes_to_non_existing_course_raise_exception(self):

        with self.assertRaises(Exception) as ex:
            self.student.add_notes("java", ["java is hard"])

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_existing_course(self):

        self.assertEqual("Course has been removed", self.student_with_courses.leave_course("python"))

    def test_leave_non_existing_course_raise_exception(self):

        with self.assertRaises(Exception) as ex:
            self.student.leave_course("java")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()
