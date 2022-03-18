
#[derive(Debug, PartialEq)]
pub struct Doller {
    pub amount: i32,
}

impl Doller {
    pub fn new(amount: i32) -> Doller {
        Doller { amount }
    }
    pub fn times(&mut self, multiplier: i32) {
        self.amount *= multiplier;
    }
}
