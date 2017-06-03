from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, color, position):
        """
        Constructor.
        :param color: string. "white" or "black"
        :param position: string. "e4", "b2" etc.
        """
        self.color = color
        self.position = position

    @abstractmethod
    def get_available_squares(self, board):
        """

        :param board: Map with an actual position
        :return: array with possible squares
        """
        pass

    @staticmethod
    def get_file(actual_file, number_of_files, go_up):
        """
        Get desired file in chessboard.
        :param actual_file:
        :param number_of_files:
        :param go_up:
        :return: corresponding file if possible, if not, return False
        """
        possible_files = ["a", "b", "c", "d", "e", "f", "g", "h"]

        if go_up:
            index = possible_files.index(actual_file)

            if index + number_of_files <= 7:
                return possible_files[index + number_of_files]

            else:
                return False
        else:
            index = possible_files.index(actual_file)

        if index - number_of_files >= 0:
            return possible_files[index - number_of_files]

        else:
            return False

