from typing import Optional, Protocol, TypeVar


A = TypeVar("A")
I_contra = TypeVar("I_contra", contravariant=True)


class CollectionOrientedRepositoryProtocol(Protocol[A, I_contra]):
    async def add(self, _aggregate: A) -> None:
        ...

    async def get(self, _id: I_contra) -> Optional[A]:
        ...

    async def delete(self, _aggregate: A) -> None:
        ...


class PersistenceOrientedRepositoryProtocol(Protocol[A, I_contra]):
    async def save(self, _aggregate: A) -> None:
        ...

    async def get(self, _id: I_contra) -> Optional[A]:
        ...

    async def delete(self, _aggregate: A) -> None:
        ...


I_co = TypeVar("I_co", covariant=True)


class GenerateIdentifierProtocol(Protocol[I_co]):
    def next_identity(self) -> I_co:
        ...
