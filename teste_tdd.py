import unittest
import requests

URL = "http://127.0.0.1:8080"

class TesteAPI(unittest.TestCase):
    def reset_dados_professor(self):
        requests.post(f"{URL}/professor", json={
            "nome": "Caio",
            "data_nascimento": "1997-04-21",
            "materia": "Desenvolvimento de APIs e Microsserviços",
            "observacoes": "Professor legal"
        })

    def resetar_dados_turma(self):
        self.reset_dados_professor()
        requests.post(f"{URL}/turma", json={
            "descricao": "Turma A",
            "professor_id": 1,
            "ativo": True
        })

    def resetar_dados_aluno(self):
        self.resetar_dados_turma()
        requests.post(f"{URL}/aluno", json={
            "nome": "Jurema",
            "data_nascimento": "1982-06-15",
            "nota_primeiro_semestre": 6.0,
            "nota_segundo_semestre": 8.0,
            "media_final": 7.0,
            "turma_id": 1
        })

    def teste01_criar_professor(self):
        resposta = requests.post(f"{URL}/professor", json={
            "nome": "Ana",
            "data_nascimento": "1989-03-10",
            "materia": "Matemática",
            "observacoes": "Muito experiente"
        })

        self.assertEqual(resposta.json()["mensagem"], "Professor adicionado com sucesso!")

    def teste02_ler_professor(self):
        resposta = requests.get(f"{URL}/professor")
        self.assertEqual(resposta.status_code, 200)
        self.assertIsInstance(resposta.json(), list)

    def teste03_ler_professor_id(self):
        resposta = requests.get(f"{URL}/professor/1")
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.json()["id"], 1)

    def teste04_atualizar_professor(self):
        resposta = requests.put(f"{URL}/professor/1", json={
            "nome": "Caio Silva",
            "data_nascimento": "1996-12-01",
            "idade": "29",
            "materia": "Desenvolvimento Web",
            "observacoes": "Agora é especialista"
        })
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.json()["nome"], "Caio Silva")

    def teste05_deletar_professor(self):
        resposta = requests.delete(f"{URL}/professor/1")
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.json()["mensagem"], "Professor deletado com sucesso!")

    def teste06_criar_turma(self):
        self.reset_dados_professor()
        resposta = requests.post(f"{URL}/turma", json={
            "descricao": "Turma de Teste",
            "professor_id": 1,
            "ativo": True
        })
        self.assertEqual(resposta.status_code, 201)
        self.assertEqual(resposta.json()["mensagem"], "Turma adicionada com sucesso!")

    def teste07_ler_turma(self):
        resposta = requests.get(f"{URL}/turma")
        self.assertEqual(resposta.status_code, 200)
        self.assertIsInstance(resposta.json(), list)

    def teste08_ler_turma_id(self):
        resposta = requests.get(f"{URL}/turma/1")
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.json()["id"], 1)

    def teste09_atualizar_turma(self):
        resposta = requests.put(f"{URL}/turma/1", json={
            "descricao": "Turma Atualizada",
            "professor_id": 1,
            "ativo": False
        })
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.json()["descricao"], "Turma Atualizada")

    def teste10_deletar_turma(self):
        resposta = requests.delete(f"{URL}/turma/1")
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.json()["mensagem"], "Turma deletada com sucesso!")

    def teste11_criar_aluno(self):
        self.resetar_dados_turma()
        resposta = requests.post(f"{URL}/aluno", json={
            "nome": "Laiane",
            "data_nascimento": "2003-12-12",
            "nota_primeiro_semestre": 8.0,
            "nota_segundo_semestre": 3.0,
            "media_final": 5.5,
            "turma_id": 1
        })

        self.assertEqual(resposta.status_code, 201)
        self.assertIn("mensagem", resposta.json())

    def teste12_ler_aluno(self):
        resposta = requests.get(f"{URL}/aluno")
        self.assertEqual(resposta.status_code, 200)
        self.assertIsInstance(resposta.json(), list)

    def teste13_ler_aluno_id(self):
        self.resetar_dados_aluno()
        resposta = requests.get(f"{URL}/aluno/1")
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.json()["id"], 1)

    def teste14_atualizar_aluno(self):
        resposta = requests.put(f"{URL}/aluno/1", json={
            "nome": "Laiane Livia",
            "data_nascimento": "2003-12-13",
            "nota_primeiro_semestre": 9.0,
            "nota_segundo_semestre": 5.0,
            "media_final": 7.0,
            "turma_id": 1
        })
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.json()["nome"], "Laiane Livia")

    def teste15_deletar_aluno(self):
        resposta = requests.delete(f"{URL}/aluno/1")
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.json()["mensagem"], "Aluno deletado com sucesso!")


def runTestes():
    rodar = unittest.defaultTestLoader.loadTestsFromTestCase(TesteAPI)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(rodar)

if __name__ == "__main__":
    runTestes()
