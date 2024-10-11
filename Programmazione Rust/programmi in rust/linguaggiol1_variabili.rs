// Variabili in RUST
// Rust tende a favorire la IMMUTABILTIA
// NON CAMBIA il suo valore

// la parola chiave: let

// per renderla modificabile : let mut

// Una volta definita DEVE SEMPRE ESSERE INIZIALIZZATA
// una costane o una espressione


let v: i32 = 123;   // Immutabile e ha tipo i32 ( intero a 32 bit con segno)

let mut w = v;      // w puo essere riassegnata, ha lo stesso tipo di v (i32)
w = -5;             // ok . ora w vale -5

let x = 1.3278;     //  x è immutabile di tipo f64 ( floating point a 64 bit)

let y = 1.327f32;   // y è immutabile di tipo f32 ( flotaing point a 32 bit)

let one_million = 1_000_000;     // si possono usare le ____ per separare le cifre

// la presenza di un espressione rappresenta un tipo:

let x = x * 2;  // espressioni vanno fatte tra tipi omogenei

// Espressioni:
// In Rust le espressioni producono un valore che puo essre usato come
// valore di ritorno per una funzione

int a = b = c = 12;     // ERROR in rust non si puo fare come in C,
                    // si possono assegnare solo 1 variabile alla volta


// RUST TIPI:

// Non cè ereditarietà in rust
// ogni tipo ha la sua specificità
// nessun legame ne gerarchia tra tipi

// Tipi Elementari:

numeriInteri = i8, i16, i32, i64, i128, isize;
numeriInteriSenzaSegno = u8, u16,u32,u64,u128,usize;

numeriInVirgolaMobile = f32, f64;

numeriLogici = bool;

nCaratteri = char; // le strinche contengono array di caratteri codificati con UTF - 8

nUnit = () // 0 elementi    -> Void di C/C++




