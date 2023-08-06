use std::str::Chars;

use crate::Spongebobizer;

pub trait Spongebobize<I: Iterator<Item = char>> {
	fn spongebobize(self) -> Spongebobizer<I>;
}

impl<'str> Spongebobize<Chars<'str>> for &'str str {
	#[inline]
	fn spongebobize(self) -> Spongebobizer<Chars<'str>> {
		Spongebobizer::from(self.chars())
	}
}

impl<I: Iterator<Item = char>> Spongebobize<I> for I {
	#[inline]
	fn spongebobize(self) -> Spongebobizer<I> {
		Spongebobizer::from(self)
	}
}

