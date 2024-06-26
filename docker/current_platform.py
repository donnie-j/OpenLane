import platform


def current_docker_platform() -> str:
    arch = platform.machine()

    if arch in ["x86_64", "amd64"]:
        return "amd64"
    elif arch in ["aarch64", "arm64"]:
        return "arm64v8"
    else:
        raise ValueError(f"Unsupported platform {arch}")


if __name__ == "__main__":
    print(current_docker_platform(), end="")
