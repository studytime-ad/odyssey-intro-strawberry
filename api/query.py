import strawberry
from .types.playlist import Playlist

# def get_hello():
#     return "Hello World"

@strawberry.type
class Query:
    # hello: str = strawberry.field(resolver=get_hello)
    
    @strawberry.field(
        description="Playlists hand-picked to be featured to all users."
    )
    def featured_playlists() -> list[Playlist]:
        return [
            Playlist(id=strawberry.ID("1"), name="GraphQL A", description=None),
            Playlist(id=strawberry.ID("2"), name="GraphQL Rock A", description=None),
            Playlist(id=strawberry.ID("3"), name="GraphQL Rock B", description=None)
        ]


