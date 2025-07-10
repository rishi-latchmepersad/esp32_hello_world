import logging
import os
import pytest
from pytest_embedded_idf.dut import IdfDut
import typing as t


@pytest.fixture
def log_minimum_free_heap_size(
    dut: IdfDut, config: str, idf_path: str
) -> t.Callable[..., None]:
    def real_func() -> None:
        res = dut.expect(r"Minimum free heap size: (\d+) bytes")
        logging.info(
            "\n------ heap size info ------\n"
            "[app_path] {}\n"
            "[app_name] {}\n"
            "[config_name] {}\n"
            "[target] {}\n"
            "[minimum_free_heap_size] {} Bytes\n"
            "------ heap size end ------".format(
                dut.app.app_path.replace(idf_path, "").lstrip("/\\"),
                os.path.basename(dut.app.app_path),
                config,
                dut.target,
                res.group(1).decode("utf8"),
            )
        )

    return real_func
