
testing.o: testing.asm
	nasm -f elf64 $< -o $@

testing: testing.o
	ld $^ -o $@

clean:
	rm *.o
	rm testing

