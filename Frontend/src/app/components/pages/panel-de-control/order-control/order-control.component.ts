import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-order-control',
  templateUrl: './order-control.component.html',
  styleUrls: ['./order-control.component.scss']
})
export class OrderControlComponent implements OnInit {

order = {
  id: 1,
  name: 'Order 1',
  date: '2020-01-01',
  status: 'Pending',
}

  constructor() { }

  ngOnInit(): void {
  }

}
