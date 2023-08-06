use criterion::BenchmarkId;
use criterion::Criterion;

use spongebobizer::process_string;

fn bench_strings(c: &mut Criterion) {
	let str_62550 = include_str!("../test/62550.txt");
	let str_7131040 = include_str!("../test/7131040.txt");
	//let str_256717510 = include_str!("../test/256717510.txt");
	c.bench_with_input(BenchmarkId::new("process_string", "lorem ipsum"), &"lorem ipsum", |b, s| b.iter(|| process_string(s)));
	c.bench_with_input(BenchmarkId::new("process_string", "abc123xyz"), &"abc123xyz", |b, s| b.iter(|| process_string(s)));
	c.bench_with_input(BenchmarkId::new("process_string", "random unicode 1"), &"8ʨ%ƴԑ:֍ыȘB\"[QןGg", |b, s| b.iter(|| process_string(s)));
	c.bench_with_input(BenchmarkId::new("process_string", "random unicode 2"), &"Hӆ͑WuƂƳ=קFե}l߆+È", |b, s| b.iter(|| process_string(s)));
	c.bench_with_input(BenchmarkId::new("process_string", "nonalphabetic"), &"1234567890)(*&^%$#@! []\\|}{';:\"/.,?><`~", |b, s| b.iter(|| process_string(s)));
	c.bench_with_input(BenchmarkId::new("process_string", "62550.txt"), &str_62550, |b, s| b.iter(|| process_string(s)));
	c.bench_with_input(BenchmarkId::new("process_string", "7131040.txt"), &str_7131040, |b, s| b.iter(|| process_string(s)));
	//c.bench_with_input(BenchmarkId::new("process_string", "256717510.txt"), str_256717510, |b, s| b.iter(|| process_str(s)));
}

criterion::criterion_group!(benches, bench_strings);
criterion::criterion_main!(benches);

