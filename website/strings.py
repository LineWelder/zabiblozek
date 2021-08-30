from backend.consts import *


ERROR_MESSAGES = {
    ERROR_AUTH_USERNAME_EXISTS: "Już mamy stronę z takim imienem",
    ERROR_AUTH_USERNAME_UNALLOWED_CHARACTERS: "Nazwa strony może składać się tylko z liter alfabetu łacińskiego i kropki",
    ERROR_AUTH_USERNAME_LENGTH: "Nazwa strony musze mieć od 2 do 30 znaków",
    ERROR_AUTH_USERNAME_CONFLICTS: "Nazwa strony konfliktuje ze stroną systemową",
    ERROR_AUTH_PASSWORD_LENGTH: "Hasło musze mieć od 6 do 30 znaków",
    ERROR_AUTH_PASSWORD_DO_NOT_MATCH: "Hasła nie zbiegają się",
    ERROR_AUTH_TITLE_LENGTH: "Tytuł strony musze mieć do 150 znaków",
    ERROR_AUTH_TITLE_EMPTY: "Proszę prowadzić tytuł strony",
    ERROR_AUTH_USERNAME_UNKNOWN: "Nie znamy strony z takim imieniem",
    ERROR_AUTH_PASSWORD_WRONG: "Hasło nie jest poprawnie",

    ERROR_USER_NOT_FOUND: "Nie znam takiej strony",

    ERROR_POST_EMPTY: "Proszę coś napisać"
}

LOGIN_MESSAGE = "Proszę się zalogować"