import subprocess

# Vulnerable function: uses shell=True in subprocess call
def run_shell_command(command):
    # This can lead to shell injection if 'command' is derived from user input
    subprocess.call(command, shell=True)

# Example usage
run_shell_command("ls -l")
