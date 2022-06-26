import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ProductsListRoutingModule } from './products-list-routing.module';
import { VrComponent } from './vr/vr.component';


@NgModule({
  declarations: [
  
    VrComponent
  ],
  imports: [
    CommonModule,
    ProductsListRoutingModule
  ]
})
export class ProductsListModule { }
