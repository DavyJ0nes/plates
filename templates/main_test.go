package main

import "testing"

func Test_exampleFunction(t *testing.T) {
	tests := []struct {
		name string
		arg  string
		want int
	}{
		{
			"test1",
			"test1",
			5,
		},
		{
			"test2",
			"",
			0,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := exampleFunction(tt.arg); got != tt.want {
				t.Errorf("got: %v, want %v", got, tt.want)
			}
		})
	}
}
