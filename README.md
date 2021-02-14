# python_trx

Controller for Radio two way - half duplex repeater. It is based on HAM radio transceiver FT-857,connected by CAT / sound card to computer (raspberry). Script periodicaly reads transceiver state - if channel is busy - start audio record - if channel is free - audio is replayed from memory and transceiver is remotely switch to TX on.
