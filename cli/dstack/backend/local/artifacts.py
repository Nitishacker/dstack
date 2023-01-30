import os
from pathlib import Path
from typing import List, Tuple, Optional, Generator

from dstack.core.repo import RepoAddress
from dstack.backend.local.common import list_objects, put_object, get_object, delete_object, list_all_objects


def dest_file_path(key: str, output_path: Path) -> Path:
    return output_path / "/".join(key.split("/")[5:])


def download_run_artifact_files(path: str, repo_address: RepoAddress,
                                run_name: str, output_dir: Optional[str]):
    pass


def list_run_artifact_files(path: str, repo_address: RepoAddress,
                            run_name: str) -> Generator[Tuple[str, str, int], None, None]:
    root = Path(path) / "artifacts" / repo_address.path()
    artifact_prefix = f"{run_name},"
    list_iterator = list_all_objects(Root=root, Prefix=artifact_prefix)
    for job_id, path, file_size in list_iterator:
        if file_size > 0:
            yield job_id, path, file_size


def __remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text


def upload_job_artifact_files(path: str, repo_address: RepoAddress, job_id: str,
                              artifact_name: str, local_path: Path):
    pass


def list_run_artifact_files_and_folders(path_backend_dir: str, repo_address: RepoAddress,
                                        job_id: str, path: str) -> List[Tuple[str, bool]]:
    pass
