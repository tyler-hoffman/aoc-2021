from unittest import TestCase, mock

from src.utils.question_asker import QuestionAsker

from .sample_data import SAMPLE_DATA
from src.day_13.b import solve

# Sorry that the expected outputs are so ugly here!
# I found the periods for empty space to be hard to look at.
# So for the sample I copy-and-pasted from the expected output
# and then replaced # periods with spaces. To backfill the solution,
# I just copy-and-pasted from my nicer-looking output.
# Oh, and we have to omit the first character here because
# it's a newline for formatting that shouldn't really be present.


def cleanup_string(string: str) -> str:
    """Helper to remove leading newline
    and potentially replace periods with blank spaces
    if present. Only exists so I can make things look
    reasonable below...
    """

    return string[1:].replace(".", " ")


expected_for_sample = cleanup_string(
    """
#####
#...#
#...#
#...#
#####
"""
)


expected_for_input = cleanup_string(
    """
###  #### #  # ###  #  # ###  #  # ### 
#  # #    #  # #  # #  # #  # # #  #  #
#  # ###  #  # #  # #  # #  # ##   #  #
###  #    #  # ###  #  # ###  # #  ### 
# #  #    #  # #    #  # #    # #  # # 
#  # ####  ##  #     ##  #    #  # #  #
"""
)


class TestDay13B(TestCase):
    """
    This one requires human input to read the characters.
    These tests mostly just verify we pass the right string to the human.
    It also verifies we return whatever the user said the string looked like
    """

    arbitrary_human_response = "dinosaur"

    def test_solve(self):
        question_asker = mock.MagicMock(spec=QuestionAsker)
        question_asker.ask.return_value = self.arbitrary_human_response

        solution = solve(SAMPLE_DATA, question_asker)

        question_asker.say.assert_called_with(expected_for_sample)
        self.assertEqual(solution, self.arbitrary_human_response)

    def test_solution(self):
        question_asker = mock.MagicMock(spec=QuestionAsker)
        question_asker.ask.return_value = self.arbitrary_human_response
        with open("src/day_13/input.txt", "r") as f:
            input_string = f.read()

        solution = solve(input_string, question_asker)

        question_asker.say.assert_called_with(expected_for_input)
        self.assertEqual(solution, self.arbitrary_human_response)
