import time

import flet as ft
from playsound import playsound

wat_words = ['Scene',
             'Impossible',
             'Society',
             'Choose',
             'Unjust',
             'Image',
             'Exam',
             'Drive',
             'Internet',
             'Communication',
             'Keys',
             'Murder',
             'Commit',
             'Flee',
             'Practice',
             'Organize',
             'Phone',
             'New',
             'Agency',
             'Security',
             'Since',
             'Peace',
             'Fall',
             'Hit',
             'Run',
             'Chase',
             'Enter',
             'Industry',
             'Limit',
             'Development',
             'Coach',
             'Food',
             'Special',
             'Biomass',
             'Release',
             'Head',
             'Launch',
             'Medal',
             'Play',
             'Department',
             'Under',
             'Curb',
             'Cooperate',
             'HIke',
             'War',
             'Normal',
             'Challenge',
             'Serving',
             'Bane',
             'Rapid',
             'Actress',
             'obstacles',
             'Strict',
             'Forceful',
             'Citizens',
             'Teams',
             'Anxious',
             'Knowledge',
             'Polite',
             'Integrity',
             'Serve',
             'Loyal',
             'Equality',
             'Justice',
             'Gratitude',
             'Rare',
             'Heavy',
             'Rude',
             'Explanation',
             'Pilot',
             'Pirate',
             'Ship',
             'Captain',
             'Camp',
             'Rights',
             'Ragging',
             'Rust',
             'Patriotism',
             'Primary',
             'Performance',
             'Pity',
             'Meeting',
             'Obedience',
             'Quick',
             'Quiet',
             'Quotes',
             'Question',
             'Try',
             'Unity',
             'Urge',
             'Friendship',
             'Close',
             'Migrate',
             'Decline',
             'Fly',
             'Highest',
             'Shallow',
             'Wipe',
             'Vegetables',
             'Sale']


def main(page: ft.Page) -> None:
    page.title = "Flet Example"
    t = ft.Text(value="Please Click Here to Start", color="Black", size=150, selectable=True)

    def change_text(e: ft.ControlEvent) -> None:
        t.selectable = False
        for i in wat_words:
            time.sleep(15)
            playsound("beep-sound-8333.mp3")
            t.value = i
            page.update()

    container = ft.Container(alignment=ft.alignment.center,
                             expand=True,
                             content=t,
                             on_click=change_text,
                             gradient=ft.LinearGradient(begin=ft.alignment.top_left,
                                                        end=ft.alignment.bottom_right,
                                                        colors=["white"]
                                                        )
                             )
    page.add(container)


ft.app(target=main)
