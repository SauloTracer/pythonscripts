class Position:
        def __init__(self, x, y, offsetX, offsetY):
                self.x = x
                self.y = y
                self.offsetX = offsetX
                self.offsetY = offsetY

        def setX(self, x):
                if (x > -1 and x <= self.offsetX):
                        self.x = x
                        return True
                return False

        def setY(self, y):
                if (y > -1 and y <= self.offsetY):
                        self.y = y
                        return True
                return False

class Player:
        def __init__(self, name, symbol):
                self.name = name
                self.symbol = symbol

class TicTacToe:

        def __init__(self):
                self.winner = None
                self.resetBoard()
                #getPlayers
                print("Informe os dados do jogador 1")
                self.player1 = self.getPlayer()

                print("Informe os dados do jogador 2")
                self.player2 = self.getPlayer()

        def resetBoard(self):
                self.board = [
                        [' ',' ',' '],
                        [' ',' ',' '],
                        [' ',' ',' ']
                ]

        def drawBoard(self):
                print ('     |     |     ')
                print ('  {}  |  {}  |  {}'.format(self.board[0][0], self.board[0][1], self.board[0][2]))
                print ('_____|_____|_____')
                print ('     |     |     ')
                print ('  {}  |  {}  |  {}'.format(self.board[1][0], self.board[1][1], self.board[1][2]))
                print ('_____|_____|_____')
                print ('     |     |     ')
                print ('  {}  |  {}  |  {}'.format(self.board[2][0], self.board[2][1], self.board[2][2]))
                print ('     |     |     ')

        def play(self, player, system=0):
                position = Position(0, 0, 2, 2)
                print(player.name)
                
                if (system == 0):
                        validEntry = False
                        n = None
                        x,y = None, None
                        while not validEntry:
                                n = input("Posição (utilize o teclado numérico): ")
                                validPositions = list(map(lambda x: str(x), list(range(1,10))))
                                if validPositions.count(n) > 0:
                                        validEntry = True
                        if int(n) > 6:
                                x = 0
                                y = int(n) - 7
                        elif int(n) > 3:
                                x = 1
                                y = int(n) - 4
                        else:
                                x = 2
                                y = int(n) - 1
                        position.setX(x)
                        position.setY(y)
                                
                else:
                        validX = validY = False
                        while (not validX):
                                try:
                                        validX = position.setX(int(input("Linha: ")));
                                        if(not validX):
                                                print ('Linha inválida.')
                                except:
                                        print ('Linha inválida.')
                                        validX = False

                        while (not validY):
                                try:
                                        validY = position.setY(int(input("Coluna: ")));
                                        if(not validY):
                                                print ('Coluna inválida.')
                                except:
                                        print ('Coluna inválida.')
                                        validX = False

                if (self.board[position.x][position.y] != ' '):
                        print('Essa posição já foi tomada!')
                        self.play(player)
                else:
                        self.board[position.x][position.y] = player.symbol
                        self.drawBoard()

        def getPlayer(self):
                name = input("Nome: ")
                symbol = input("Símbolo: ")
                while (symbol == ' '):
                        symbol = input("Símbolo: ")
                return Player(name, symbol)

        def run(self):
                self.drawBoard()

                endGame = False
                playersTurn = self.player1

                while (not endGame):
                        self.play(playersTurn)
                        playersTurn = self.player2 if (playersTurn == self.player1) else self.player1
                        endGame = self.gameOver()
                else:
                        self.showResult()
                        self.resetBoard()
                        self.winner = None
                        self.run()

        def testLine(self, linha):
                s = self.board[linha][0]
                if (self.board[linha].count(s) == 3):
                        if(s != ' '):
                                self.winner = self.player1 if (s == self.player1.symbol) else self.player2
                                return True
                return False

        def testColumn(self, column):
                s = self.board[0][column]

                c = []
                for x in range(len(self.board[0])):
                        c.append(self.board[x][column])

                if (c.count(s) == 3):
                        if(s != ' '):
                                self.winner = self.player1 if (s == self.player1.symbol) else self.player2
                                return True

                return False

        def testDiagonals(self):
                diagonals = [[],[]]
                for x in range(len(self.board)):
                        for y in range(len(self.board[x])):
                                if(x == y):
                                        diagonals[0].append(self.board[x][y])
                                if((x + y) == len(self.board)-1):
                                        diagonals[1].append(self.board[x][y])

                s = diagonals[0][0]
                if (diagonals[0].count(s) == 3):
                        if (s != ' '):
                                self.winner = self.player1 if (s == self.player1.symbol) else self.player2
                                return True

                s = diagonals[1][0]
                if (diagonals[1].count(s) == 3):
                        if (s != ' '):
                                self.winner = self.player1 if (s == self.player1.symbol) else self.player2
                                return True

                return False

        def gameOver(self):
                for x in range(len(self.board)):
                        lineResult = self.testLine(x)
                        if(lineResult):
                                return True

                if (self.winner is None):
                        for y in range(len(self.board[0])):
                                columnResult = self.testColumn(y)
                                if (columnResult):
                                        return True

                if (self.winner is None):
                        diagResult = self.testDiagonals()
                        if (diagResult):
                                return True

                count = 0
                for x in range(len(self.board)):
                        count += self.board[x].count(' ')

                if (count == 0):
                        return True

                return False

        def showResult(self):
                if (self.winner is None):
                        print('O jogo terminou em um empate!')
                else:
                        print('\\o/ {} ganhou! \\o/'.format(self.winner.name))

game = TicTacToe();
game.run()
