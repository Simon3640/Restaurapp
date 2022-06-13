import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {

  @Input() Nproducts : number = 0;
  @Output() clickCart : EventEmitter<string> = new EventEmitter<string>();
  
  clickCartEvent() {
    this.clickCart.emit('cart');
  }


  constructor() { }

  ngOnInit(): void {
  }

}
