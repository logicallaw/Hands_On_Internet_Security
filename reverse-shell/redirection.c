#include <fcntl.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

int main() {
  int fd0, fd1;
  char input[100];

  fd0 = open("/tmp/input", O_RDONLY);
  fd1 = open("/tmp/output", O_RDWR);

  dup2(fd0, 0); // 표준 입력을 /tmp/input으로
  dup2(fd1, 1); // 표준 출력을 /tmp/output으로

  memset(input, 0, 100);
  read(0, input, 100);
  write(1, input, 100);

  close(fd0);
  close(fd1);

  return 0;
}