	.global alu
	.intel_syntax noprefix
	.text
alu:
	.rept REPEAT_COUNT
	addq    rsi, rdi
	popcnt  rax, rsi
	.endr

	ret

