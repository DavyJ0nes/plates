package main

import "testing"

func Test_exampleFunction(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			"test1",
			args{"test1"},
			5,
		},
		{
			"test2",
			args{""},
			0,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := exampleFunction(tt.args.s); got != tt.want {
				t.Errorf("exampleFunction() = %v, want %v", got, tt.want)
			}
		})
	}
}
