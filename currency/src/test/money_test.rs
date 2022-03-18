use crate::doller::Doller;


#[test]
fn multiplication() {
    let mut five = Doller::new(5);
    five.times(2);
    assert_eq!(10, five.amount);
}
