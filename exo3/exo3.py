"""
Une méthode agile est une approche itérative et collaborative pour
mener à bien un projet.
Elle génère un produit de haute qualité tout en prenant en compte
l’évolution des besoins des clients.

La méthode la plus connue est Scrum.

Au début d'un projet un « backlog », ensemble de tache à réaliser
est défini avec le client.
Ce « backlog » évolue dans le temps en fonction du besoin de client.
On peut y rajouter des taches comme on peut en enlever.

Durant le projet, une réunion avec l'équipe technique et l'équipe
opérationnelle est organisée à chaque
« sprint » (unité de temps composé de quelques semaines).
Lors cette réunion, le client valide ou non les taches
qui ont été réalisées durant la période de « sprint ».
class Task:
    def __init__(self, name, is_completed=False):
        self.name = name
        self.is_completed = is_completed

    def complete(self):
        self.is_completed = True

class Backlog:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        task = Task(task_name)
        self.tasks.append(task)
        print(f"Tâche ajoutée : {task_name}")

    def remove_task(self, task_name):
        self.tasks = [task for task in self.tasks if task.name != task_name]
        print(f"Tâche supprimée : {task_name}")

    def show_tasks(self):
        print("Backlog des tâches :")
        for task in self.tasks:
            status = "Terminée" if task.is_completed else "À faire"
            print(f"- {task.name}: {status}")

class Sprint:
    def __init__(self, backlog):
        self.backlog = backlog

    def perform_sprint(self):
        print("\nDébut du sprint !")
        self.backlog.show_tasks()

        for task in self.backlog.tasks:
            task.complete()  # Simulons la réalisation de chaque tâche
            print(f"Tâche réalisée : {task.name}")

        print("\nSprint terminé !")
        self.backlog.show_tasks()

# Simulation de l'approche agile
if __name__ == "__main__":
    # Création du backlog
    backlog = Backlog()
    backlog.add_task("Développer la fonctionnalité A")
    backlog.add_task("Tester la fonctionnalité A")
    backlog.add_task("Déployer la fonctionnalité A")

    # Exécution du sprint
    sprint = Sprint(backlog)
    sprint.perform_sprint()


Dans ce challenge, vous devez déterminer si à la date de la livraison
finale, le client obtient la totalité de son produit.


Format des données

Entrée
Ligne 1 : un entier N correspondant au nombre de sprints(réunion).
Ligne 2 : un entier T correspondant au nombre de taches dans le « backlog »
        initial.
Ligne 3 à N+2 : un entier V et un entier U séparés par un espace où V est
le nombre de taches validées
et U le nombre de taches à ajouter (si U est positif) ou à supprimer
(si U est négatif) dans le « backlog ».

Sortie
La chaîne OK si le backlog est vide. Sinon retourner la chaîne KO.

"""


def processLines(lines) -> str:
    # Implementer votre réponse ici
    return "OK"
