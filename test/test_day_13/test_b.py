from unittest import TestCase, mock

from src.utils.question_asker import QuestionAsker

from .sample_data import SAMPLE_DATA
from src.day_13.b import solve

# Sorry that the expected outputs are so ugly here!
# I found the periods for empty space to be hard to look at
# so I copy-and-pasted from the sample output and then replaced
# periods with spaces, but to backfill the solution, I just
# copy-and-pasted from my prettier output.
# Oh, and we have to omit the first character here because
# it's a newline for formatting that shouldn't really be present.

EXPECTED_FOR_SAMPLE = """
#####
#...#
#...#
#...#
#####
"""[
    1:
].replace(
    ".", " "
)

EXPECTED_FOR_INPUT = """
###  #### #  # ###  #  # ###  #  # ### 
#  # #    #  # #  # #  # #  # # #  #  #
#  # ###  #  # #  # #  # #  # ##   #  #
###  #    #  # ###  #  # ###  # #  ### 
# #  #    #  # #    #  # #    # #  # # 
#  # ####  ##  #     ##  #    #  # #  #
"""[
    1:
]


class TestDay13B(TestCase):
    """
    This one requires human input to read the characters.
    These tests just verifies we pass the right string to the human.
    """

    def test_solve(self):
        question_asker = mock.MagicMock(spec=QuestionAsker)

        solve(SAMPLE_DATA, question_asker)

        question_asker.say.assert_called_with(EXPECTED_FOR_SAMPLE)

    def test_solution(self):
        with open("src/day_13/input.txt", "r") as f:
            input_string = f.read()

        question_asker = mock.MagicMock(spec=QuestionAsker)

        solve(input_string, question_asker)

        question_asker.say.assert_called_with(EXPECTED_FOR_INPUT)
