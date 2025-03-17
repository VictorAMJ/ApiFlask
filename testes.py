import unittest
import requests

URL = "http://127.0.0.1:5000"

class TesteAPI(unittest.TestCase):
    def reset_dados_professor(self):
        requests.post(f"{URL}/professor", json= {
            "id": 1,
            "idade": 27,
            "materia": "Desenvolvimento de APIs e Microsserviços",
            "nome": "Caio",
            "observacoes": "Professor legal"
        })

    def resetar_dados_turma(self):
        requests.post(f"{URL}/turma", json={
            "id": 1,
            "descricao": "nenhuma",
            "professor_id": 1, 
            "ativo": True
        })

    def teste01_criar_professor(self):
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


    def teste02_ler_professor(self):
        resposta = requests.get(f"{URL}/professor")

        self.assertEqual(resposta.status_code, 200, "Erro ao listar professores!")
        self.assertTrue(isinstance(resposta.json(), list), "A resposta não é uma lista!")


    def teste03_atualizar_professor(self):
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


    def teste04_deletar_professor(self):
        resposta = requests.delete(f"{URL}/professor/1")

        self.assertEqual(resposta.status_code, 200, "Erro ao deletar Professor!")
        self.assertEqual(resposta.json()["mensagem"], "Professor deletado com sucesso!")


    def teste09_criar_turma(self):
        resposta = requests.post(f"{URL}/turma", json={
            "id": 2,
            "descricao": "nenhuma",
            "professor_id": 2, 
            "ativo": True
        })

        self.assertEqual(resposta.status_code, 201, "Erro ao criar Turma!")

        self.assertEqual(resposta.json()["id"], 2, "Erro ao criar o ID de turma!")

        self.assertEqual(resposta.json()["descricao"], "nenhuma", "Erro ao criar a descrição!")

        self.assertEqual(resposta.json()["professor_id"], 2, "Erro ao encontar professor!")

        self.assertEqual(resposta.json()["ativo"], True, "Erro, a turma não está ativa!")

    def teste10_listar_turma(self):
        resposta = requests.get(f"{URL}/turma")

        self.assertEqual(resposta.status_code, 200, "Erro ao listar turma!")

        self.assertTrue(isinstance(resposta.json(), list), "A resposta não é uma lista!")

    def teste11_atualizar_turma(self):
        resposta = requests.put(f"{URL}/turma/2", json={
            "id": 2,
            "descricao": "uma turma divertida",
            "professor_id": 2, 
            "ativo": True
        })

        self.assertEqual(resposta.status_code, 200, "Erro ao atualizar turma!")

        self.assertEqual(resposta.json()["id"], 2, "Erro ao atualizar o ID da turma!")

        self.assertEqual(resposta.json()["descricao"], "uma turma divertida", "Erro ao atualizar a descrição da turma!")

        self.assertEqual(resposta.json()["professor_id"], 2, "Erro ao atualizar professor!")

        self.assertEqual(resposta.json()["ativo"], True, "Erro ao ativar a turma!")

    def teste12_deletar_turma(self):
        resposta = requests.delete(f"{URL}/turma/1")

        self.assertEqual(resposta.status_code, 200, "Erro ao deletar turma!")

        self.assertEqual(resposta.json()["mensagem"], "Turma deletado com sucesso.")





def runTestes():
    rodar = unittest.defaultTestLoader.loadTestsFromTestCase(TesteAPI)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(rodar)

if __name__ == "__main__":
    runTestes()