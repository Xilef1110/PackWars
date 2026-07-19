{
  pkgs,
  lib,
  ...
}:

{
  languages.python = {
    enable = true;
    uv = {
      enable = true;
      sync.enable = true;
    };
  };

  scripts.hello.exec = "uv run python hello.py";

  enterShell = ''
    . .devenv/state/venv/bin/activate
    hello
  '';
  # See full reference at https://devenv.sh/reference/options/
}
