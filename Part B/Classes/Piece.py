from Enums.Player import Player


class Piece():
    """
    A structure that represents a piece on the board.
    """

    # The player that the piece belongs to.
    owner: Player

    # This is a counter used to uniquely identify every instance of Piece in the
    # game. This comes into play when a piece jumps over an enemy piece. We want
    # to ensure that the piece that ends up on the other side of the enemy piece
    # is not the same from the original position (see implementation of
    # board._get_killed_positions()).
    _id: int = 0

    def __init__(self, owner: Player):
        self.owner = owner
        self._id = Piece._id
        Piece._id += 1

    def getRepresentation(self):
        """
        Returns the string representation for the piece. Expected use would be
        for printing the board that the square (which has this piece) is a part
        of.
        """
        return self.owner.getRepresentation()

    def __eq__(self, other: 'Piece'):
        """
        Compares two piece objects.
        """
        return self._id == other._id
