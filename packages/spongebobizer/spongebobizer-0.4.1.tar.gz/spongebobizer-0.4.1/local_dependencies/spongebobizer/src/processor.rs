use std::iter::FusedIterator;

use crate::core::convert_char;
use crate::core::AlphaCase;
use crate::core::Char;

pub struct Spongebobizer<I: Iterator<Item = char>> {
	chars: I,
	current_char: Option<Char>,
	sum: u32,
	prev: AlphaCase,
	pprev: AlphaCase,
}

impl<I: Iterator<Item = char>> From<I> for Spongebobizer<I> {
	#[inline]
	fn from(chars: I) -> Self /* {{{ */ {
		Self{
			chars,
			current_char: None,
			sum: 0,
			prev: AlphaCase::Upper,
			pprev: AlphaCase::Lower
		}
	} // }}}
}

impl<I: Iterator<Item = char>> Iterator for Spongebobizer<I> {
	type Item = char;

	#[inline]
	fn next(&mut self) -> Option<Self::Item> {
		if let Some(c) = self.current_char.as_mut().and_then(|c| c.next()) {
			return Some(c);
		}

		let c = self.chars.next()?;
		self.sum = (self.sum + c as u32) & 0x07;
		if(!c.is_alphabetic()) {
			self.current_char = Some(c.into());
		} else if(self.prev == self.pprev) {
			self.pprev = self.prev;
			self.prev.negate();
			self.current_char = Some(convert_char(c, &self.prev));
		} else {
			self.pprev = self.prev;
			if(self.sum > 0) {
				self.prev.negate();
			}
			self.current_char = Some(convert_char(c, &self.prev));
		}
		self.next()
	}

	#[inline]
	fn size_hint(&self) -> (usize, Option<usize>) /* {{{ */ {
		let size = self.chars.size_hint();
		(size.0, size.1.map(|s| s * 3))
	} // }}}
}

impl<I: Iterator<Item = char> + FusedIterator> FusedIterator for Spongebobizer<I> {}

