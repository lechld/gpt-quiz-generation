from enum import Enum

class QuestionCategory(Enum):
    GENERAL_KNOWLEDGE = (9, "General knowledge questions")
    ENTERTAINMENT_BOOKS = (10, "Questions about books and literature")
    ENTERTAINMENT_FILM = (11, "Questions about films and cinema")
    ENTERTAINMENT_MUSIC = (12, "Questions about music and artists")
    ENTERTAINMENT_MUSICALS_THEATRES = (13, "Questions about musicals and theatres")
    ENTERTAINMENT_TELEVISION = (14, "Questions about television shows and series")
    ENTERTAINMENT_VIDEO_GAMES = (15, "Questions about video games")
    ENTERTAINMENT_BOARD_GAMES = (16, "Questions about board games")
    SCIENCE_NATURE = (17, "Questions about science and nature")
    SCIENCE_COMPUTERS = (18, "Questions about computers and technology")
    SCIENCE_MATHEMATICS = (19, "Questions about mathematics and numbers")
    MYTHOLOGY = (20, "Questions about mythology")
    SPORTS = (21, "Questions about sports and athletes")
    GEOGRAPHY = (22, "Questions about geography and landmarks")
    HISTORY = (23, "Questions about history and events")
    POLITICS = (24, "Questions about politics and government")
    ART = (25, "Questions about art and artists")
    CELEBRITIES = (26, "Questions about celebrities")
    ANIMALS = (27, "Questions about animals and wildlife")
    VEHICLES = (28, "Questions about vehicles and transportation")
    ENTERTAINMENT_COMICS = (29, "Questions about comics and graphic novels")
    SCIENCE_GADGETS = (30, "Questions about gadgets and devices")
    ENTERTAINMENT_ANIME_MANGA = (31, "Questions about Japanese anime and manga")
    ENTERTAINMENT_CARTOON_ANIMATIONS = (32, "Questions about cartoons and animations")

    def __init__(self, otdb_id, llm_description):
        self.otdb_id = otdb_id
        self.llm_description = llm_description

    @classmethod
    def get_category_by_name(cls, name):
        for category in cls:
            if category.name == name.upper():
                return category
        raise ValueError(f"Category {name} not found.")