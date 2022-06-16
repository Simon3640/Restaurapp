import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ProductPanelRoutingModule } from './product-panel-routing.module';
import { NgSelectModule } from '@ng-select/ng-select';


@NgModule({
  declarations: [
  ],
  imports: [
    CommonModule,
    ProductPanelRoutingModule,
    NgSelectModule
  ]
})
export class ProductPanelModule { }
