{ pkgs }: {
  deps = [
    pkgs.neofetch
    pkgs.nodePackages.vscode-langservers-extracted
    pkgs.nodePackages.typescript-language-server  
  ];
}