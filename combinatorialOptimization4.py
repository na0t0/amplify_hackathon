import sys # 引数取得
import argparse # 引数をリストで

from amplify import *

# import amplify # add
# from amplify import(
#     gen_symbols,
#     IsingPoly,
# )
from amplify.client import FixstarsClient
# from amplify import Solver
# from amplify import decode_solution

def comb1_main(A):

    # 数の集合Aに対応する数のリスト
    # A = [2, 10, 3, 8, 5, 7, 9, 5, 3, 2]
    print(A)

    # len(A): 変数の数
    n = len(A)

    # イジング変数を生成 
    s = gen_symbols(IsingPoly, n)

    # 変数を確認
    print(s)

    # 目的関数の構築: イジング
    f = IsingPoly()

    for i in range(n):
        # f += s[i] * A[i]
        f += s[i] * int(A[i])

    f = f ** 2

    # クライアントの設定
    client = FixstarsClient()
    client.parameters.timeout = 1000   # タイムアウト1秒
    # client.token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # ローカル環境で使用する場合は、Amplify AEのアクセストークンを入力してください
    client.parameters.outputs.duplicate = True  # 同じエネルギー値の解を列挙

    solver = Solver(client)
    result = solver.solve(f)

    # 解が得られなかった場合、len(result) == 0
    if len(result) == 0:
        raise RuntimeError("No solution was found")
        
    energy = result[0].energy
    values = result[0].values

    # エネルギー値 (f の最小値) を確認
    print(f"f = {energy}")

    # valuesを確認
    # 変数 s_i の i=0, 1, ..., N-1 の値を格納した辞書
    print(f"values = {values}")
    solution = decode_solution(s, values)

    print(solution)

    A0 = sorted([A[idx] for idx, val in enumerate(solution) if val != 1])
    A1 = sorted([A[idx] for idx, val in enumerate(solution) if val == 1])

    print(f"A0 = {A0}")
    print(f"A1 = {A1}")

    Res0 = f"{A0}" 
    Res1 = f"{A1}"

    return Res0, Res1
