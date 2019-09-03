import FilmyKeeda.FilmyKeeda as Keeda
import os

path = os.path.join(os.getcwd(),"Data","A_Few_Good_Men.txt")


scriptWriter = Keeda.getWriter("GPT2")
results = evaluator = Keeda.getEvaluator(
    scriptWriter,
    textPath=path,
    evalType="ROUGE"
)