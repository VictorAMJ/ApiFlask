import unittest
import requests

URL = "http://127.0.0.1:5000"

class TesteAPI(unittest.TestCase):
    def reset_dados(self):
        requests.post(f"{URL}/professor", json= {
            "id": 1,
            "idade": 27,
            "materia": "Desenvolvimento de APIs e Microsserviços",
            "nome": "Caio",
            "observacoes": "Professor legal"
        })

    def teste1_criar_professor(self):
        resposta = requests.post(f"{URL}/professor", json= {
            "id": 2,
            "nome": "Ana",
            "idade": 35,
            "materia": "Matemática",
            "observacoes": "Muito experiente"
        })

        self.assertEqual(resposta.status_code, 201, "Erro ao criar Professor!")

        self.assertEqual(resposta.json()["id"], 2, "Erro ao criar Id de Professor!")

        self.assertEqual(resposta.json()["nome"], "Ana", "Erro ao criar Nome de Professor!")

        self.assertEqual(resposta.json()["idade"], 35, "Erro ao criar Idade de Professor!")

        self.assertEqual(resposta.json()["materia"], "Matemática", "Erro ao criar Matéria de Professor!")

        self.assertEqual(resposta.json()["observacoes"], "Muito experiente", "Erro ao criar Observações de Professor!")

    def teste2_ler_professor(self):
        resposta = requests.get(f"{URL}/professor")

        self.assertEqual(resposta.status_code, 200, "Erro ao listar professores!")
        self.assertTrue(isinstance(resposta.json(), list), "A resposta não é uma lista!")

    def teste3_atualizar_professor(self):
        resposta = requests.put(f"{URL}/professor/1", json={
            "id": 1,
            "nome": "Caio Silva",
            "idade": 28,
            "materia": "Desenvolvimento Web",
            "observacoes": "Agora é especialista"
        })

        self.assertEqual(resposta.status_code, 200, "Erro ao atualizar Professor!")

        self.assertEqual(resposta.json()["id"], 1, "O id de Professor não foi atualizado")

        self.assertEqual(resposta.json()["nome"], "Caio Silva", "O nome do Professor não foi atualizado")

        self.assertEqual(resposta.json()["idade"], 28, "A idade de Professor não foi atualizado!")

        self.assertEqual(resposta.json()["materia"], "Desenvolvimento Web", "A matéria de Professor não foi atualizada!")

        self.assertEqual(resposta.json()["observacoes"], "Agora é especialista", "As observações de Professor não foram atualizadas!")

    def teste4_deletar_professor(self):
        resposta = requests.delete(f"{URL}/professor/1")

        self.assertEqual(resposta.status_code, 200, "Erro ao deletar Professor!")
        self.assertEqual(resposta.json()["mensagem"], "Professor deletado com sucesso!")






def runTestes():
    rodar = unittest.defaultTestLoader.loadTestsFromTestCase(TesteAPI)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(rodar)

if __name__ == "__main__":
    runTestes()