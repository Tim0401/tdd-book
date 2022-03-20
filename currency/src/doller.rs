
#[derive(Debug, PartialEq)]
pub struct Doller {
    pub amount: i32,
}

impl Doller {
    pub fn new(amount: i32) -> Doller {
        Doller { amount }
    }
    pub fn times(& self, multiplier: i32) -> Doller {
        return Doller::new(self.amount * multiplier);
    }
}

#[test]
fn multiplication() {
    let five = Doller::new(5);
    let product = five.times(2);
    assert_eq!(10, product.amount);
    let product = five.times(3);
    assert_eq!(15, product.amount);
}

#[test]
fn equality() {
    assert_eq!(Doller::new(5), Doller::new(5));
    assert_ne!(Doller::new(5), Doller::new(6));
}